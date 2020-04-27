#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author: Loreto Parisi (loretoparisi at gmail dot com)
# Code: https://github.com/loretoparisi/contacttracing
# adapted from: https://github.com/gretelai/contact-tracing-experiment
#

import random, json
import datetime
from typing import List

from handset import Handset, Contact, TEK
try:
    from .handset import Handset, Contact, TEK
except:
    from handset import Handset, Contact, TEK


def get_handsets(count, relation):
    return [Handset(relation) for _ in range(0, count)]


class Cloud:

    def __init__(self):
        self.diagnosis_keys = []

    def add_tek(self, tek: TEK):
        self.diagnosis_keys.append(tek)


class Life:

    def __init__(self, start_time: int,
        family_range,
        friends_range,
        coworkers_range,
        others_range):

        self.ONE_HOUR = 3600 # cannot be changed
        self.ONE_DAY = 86400

        self.family = get_handsets(family_range, 'family')
        self.friends = get_handsets(friends_range, 'friend')
        self.coworkers = get_handsets(coworkers_range, 'coworker')
        self.others = get_handsets(others_range, 'other')

        self.all_handsets = self.family + self.friends + self.coworkers + self.others  # noqa

        # this is the current date/time for the simulation
        self.time = start_time

        # save off the actual start time for reporting
        self.start_time_ts = start_time
        self.start_time = datetime.datetime.utcfromtimestamp(start_time).isoformat()  # noqa

        # the person that eventually will contract C19
        self.subject = Handset('subject')

        self.cloud = Cloud()

    def start(self):
        """This is the main entrypoint for running the simulation, the
        called functions here are just helpers to create common patterns
        of interaction
        """
        for _ in range(0, 5):
            self.weekday()

        self.weekend()
        self.weekend()

        for _ in range(0, 5):
            self.weekday()

        self.weekend()
        self.weekend()

        # save off the actual end time for reporting
        self.end_time = datetime.datetime.utcfromtimestamp(self.time).isoformat()  # noqa

        self.subject.upload_teks(self.cloud)

    def find_contacts(self):
        """Go through all of the handsets and find
        which ones were in contact
        """
        contacts = []
        for handset in self.all_handsets:
            contacts.append(handset.determine_contacts(self.cloud))
        return sorted(contacts, key=lambda c: len(c), reverse=True)

    def mingle(self, other: Handset):
        subject_rpi = self.subject.get_rpi(self.time)
        other_rpi = other.get_rpi(self.time)

        other.receive_rpi(subject_rpi)
        self.subject.receive_rpi(other_rpi)

    def generate_report(self):

        # report statistics
        stats = {}
        stats['start_time'] = self.start_time
        stats['end_time'] = self.end_time
        stats['hour_duration_sec'] = self.ONE_HOUR
        stats['day_duration_sec'] = self.ONE_DAY
        stats['contacts'] = 0
        stats['contact_periods'] = 0

        ts = datetime.datetime.utcfromtimestamp(self.start_time_ts)
        fname = 'report_' + ts.strftime('%Y-%m-%dT%H%M%S') + '.txt'

        with open(fname, 'w') as fp:

            stats['family'] = len(self.family)
            stats['friends'] = len(self.friends)
            stats['coworkers'] = len(self.coworkers)
            stats['others'] = len(self.others)

            fp.write(f'Simulation Start Time: {self.start_time}\n\n')
            fp.write(f'Family Count: {len(self.family)}\n')
            fp.write(f'Friend Count: {len(self.friends)}\n')
            fp.write(f'Coworker Count: {len(self.coworkers)}\n')
            fp.write(f'Other Count: {len(self.others)}\n\n')

            contacts = self.find_contacts()
            contact_list: List[Contact]
            for contact_list in contacts:
                if not contact_list:
                    continue
                stats['contacts'] = stats['contacts'] + 1
                # write metadata about the handset using the first Contact
                fp.write('-'*20 + '\n')
                fp.write(f'Handset ID: {contact_list[0].uuid}\n')
                fp.write(f'Relation to subject: {contact_list[0].relation}\n')
                fp.write(f'Contact periods:\n')
                # write out the timestamps this handset had close
                # contact with the subject
                for contact in contact_list:
                    fp.write(f'\t\t{contact.ts}\n')
                    stats['contact_periods'] = stats['contact_periods'] + 1
        
        return json.dumps(stats, sort_keys=False, indent=4)

    def hour(self, focus: str):

        self.time += self.ONE_HOUR

        if focus == 'family':
            other = random.choice(self.family)
            self.mingle(other)

        if focus == 'coworker':
            other = random.choice(self.coworkers)
            self.mingle(other)
            other = random.choice(self.coworkers)
            self.mingle(other)

        if focus == 'friends':
            other = random.choice(self.friends)
            self.mingle(other)

        if focus == 'others':
            other = random.choice(self.others)
            self.mingle(other)

    def weekday(self):
        day_start = self.time  # save the first hour of our day

        # starting a new day, generate the TEK
        # for each handset

        self.subject.create_tek(self.time)

        for h in self.all_handsets:
            h.create_tek(self.time)

        # 1h at home with family
        self.hour('family')

        # 1h commute / breakfast
        if random.choice([1, 2, 3]) == 1:
            self.hour('others')

        # 4h work
        self.hour('coworker')
        self.hour('coworker')
        self.hour('coworker')
        self.hour('coworker')

        # 1h lunch / gym
        if random.choice([1, 2, 3]) == 1:
            self.hour('others')

        # 4h work
        self.hour('coworker')
        self.hour('coworker')
        self.hour('coworker')
        self.hour('coworker')

        # 1h happy hour
        if random.choice([1, 2, 3, 4, 5]) == 1:
            self.hour('friends')

        # 2h back home
        self.hour('family')
        self.hour('family')

        # fast forward to the next morning
        self.time = day_start + self.ONE_DAY

    def weekend(self):
        day_start = self.time

        self.subject.create_tek(self.time)

        for h in self.all_handsets:
            h.create_tek(self.time)

        # 2h wakeup home
        self.hour('family')
        self.hour('family')

        # 1h gym
        self.hour('others')

        # 1h quick meetup
        self.hour('friends')

        # 2h lunch home
        self.hour('family')
        self.hour('family')

        # party
        self.hour('friends')
        self.hour('friends')

        # afterparty
        self.hour('others')
        self.hour('others')

        # 1h family
        self.hour('family')
        self.hour('family')

        self.time = day_start + self.ONE_DAY
