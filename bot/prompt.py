#!/usr/bin/env python3
import random
from collections import Counter
from .typos import add_typos

def random_select_weighted_list(ls):
    return random.choices([k[1] for k in ls], weights = [k[0] for k in ls], k = 1)[0]

suspect_words = [
    (1.0, 'know'),
    (1.0, 'determined'),
    (1.0, 'have determined'),
    (1.0, 'discovered'),
    (1.0, 'uncovered'),
    (1.0, 'suspect'),
    (1.0, 'learned'),
    (0.8, 'figured out'),
    (1.0, 'found out'),
    (1.0, 'can show'),
    (1.0, 'can reveal'),
    (1.0, 'have revealed'),
    (1.0, 'revealed'),
    (1.0, 'revealed proof'),
    (1.0, 'revealed evidence'),
    (1.0, 'revealed information'),
    (0.5, 'have reason to suspect'),
    (1.0, 'have information'),
    (1.0, 'got information'),
    (1.0, 'found information'),
    (1.0, 'obtained information'),
    (1.0, 'believe'),
    (0.5, 'have reason to believe'),
    (1.0, 'think'),
    (0.5, 'have found evidence'),
    (0.5, 'have written evidence'),
    (0.5, 'have audio evidence'),
    (0.5, 'have video evidence'),
    (0.5, 'have obtained evidence'),
    (0.5, 'have evidence'),
    (0.5, 'have strong evidence'),
    (1.0, 'am convinced'),
    (1.0, 'am certain'),
    (1.0, 'am positive'),
    (1.0, 'am suspicious'),
    (1.0, 'am sure'),
    (1.0, 'am reporting'),
    (1.0, 'am testifying'),
    (1.0, 'am notifying'),
    (1.0, 'hereby report'),
    (1.0, 'can prove'),
    (0.8, 'can legally show'),
    (0.8, 'can legally prove'),
    (1.0, 'can verify'),
    (0.3, 'can attest'),
    (0.5, 'can testify'),
    (0.5, 'will testify'),
    (1.0, 'have verified'),
    (1.0, 'have verification'),
    (1.0, 'got verification'),
    (0.8, 'happened upon proof'),
    (0.8, 'happened upon evidence'),
    (0.8, 'happened upon information'),
    (0.8, 'stumbled upon proof'),
    (0.8, 'stumbled upon evidence'),
    (0.8, 'stumbled upon information'),
    (0.8, 'came upon proof'),
    (0.8, 'came upon evidence'),
    (0.8, 'came upon information'),
    (0.8, 'came across evidence'),
    (0.8, 'came across proof'),
    (0.8, 'came across information'),
    (1.0, 'offer proof'),
    (1.0, 'offer evidence'),
    (1.0, 'offer information'),
    (1.0, 'uncovered evidence'),
    (1.0, 'uncovered information'),
    (1.0, 'recovered proof'),
    (1.0, 'recovered evidence'),
    (0.5, 'just received proof'),
    (0.5, 'just received evidence'),
    (1.0, 'got evidence'),
    (1.0, 'just got evidence'),
    (1.0, 'just got proof'),
    (1.0, 'got proof'),
    (1.0, 'received proof'),
    (1.0, 'received evidence'),
    (1.0, 'received information'),
    (1.0, 'got hold of proof'),
    (1.0, 'got hold of evidence'),
    (1.0, 'got hold of information'),
    (1.0, 'saved proof'),
    (1.0, 'saved evidence'),
    (1.0, 'saved information'),
    (1.0, 'stored proof'),
    (1.0, 'stored evidence'),
    (1.0, 'stored information'),
    (1.0, 'uncovered proof'),
    (0.5, 'have saved proof'),
    (0.5, 'have saved evidence'),
    (0.5, 'happen to have proof'),
    (0.5, 'happen to have evidence'),
    (0.8, 'hold the proof'),
    (0.8, 'hold the evidence'),
    (0.8, 'have the evidence'),
    (1.0, 'have the proof'),
    (1.0, 'have proof'),
    (0.5, 'will prove'),
    (0.5, 'will legally prove'),
    (0.5, 'will provide proof'),
    (0.5, 'will show legal proof'),
    (0.5, 'have it on video'),
    (0.5, 'have it on film'),
    (0.5, 'have it on recording'),
    (1.0, 'have video proof'),
    (1.0, 'have audio proof'),
    (0.5, 'saved screenshots to prove'),
    (0.5, 'saved screenshots for evidence'),
    (0.5, 'saved texts as proof'),
    (0.5, 'saved texts as evidence'),
    (0.5, 'saved messages to document'),
    (0.5, 'saved messages showing evidence'),
    (0.8, 'took screenshot evidence'),
    (0.8, 'took screenshots proving'),
    (0.8, 'saved video proof'),
    (0.8, 'took video as documentation'),
    (1.0, 'have confirmed'),
    (1.0, 'have confirmation'),
    (1.0, 'know and can prove'),
    (1.0, 'know and may reveal'),
    (1.0, 'know and can show'),

]
my_family_words = [
    (0.5, 'dad'),
    (0.5, 'mom'),
    (0.5, 'god-father'),
    (0.5, 'god father'),
    (0.5, 'godfather'),
    (0.5, 'father'),
    (0.5, 'mother'),
    (0.5, 'god-mother'),
    (0.5, 'god mother'),
    (0.5, 'godmother'),
    (1.0, 'brother'),
    (1.0, 'sister'),
    (0.2, 'older brother'),
    (0.2, 'older sister'),
    (0.5, 'younger brother'),
    (0.5, 'younger sister'),
    (1.0, 'cousin'),
    (2.0, 'aunt'),
    (0.5, 'uncle'),
    (0.6, 'daughter'),
    (0.6, 'son'),
    (0.2, 'step-son'),
    (0.1, 'step son'),
    (0.2, 'step-daughter'),
    (0.1, 'step daughter'),
    (0.7, 'nephew'),
    (0.7, 'niece'),
    (0.5, 'grandmother'),
    (0.5, 'gram'),
    (0.2, 'grammy'),
    (0.5, 'oma'),
    (0.2, 'grandma'),
    (0.5, 'grandfather'),
    (0.5, 'opa'),
    (0.2, 'grandpa'),
    (0.5, 'granddad'),
    (1.0, 'grandson'),
    (1.0, 'granddaughter'),
    (1.0, 'son-in-law'),
    (1.0, 'daughter-in-law'),
    (1.0, 'mother-in-law'),
    (1.0, 'father-in-law'),
    (0.1, 'half-brother'),
    (0.1, 'half-sister'),
]
subjects = [
    'science',
    'math',
    'history',
    'social studies',
    'chemistry',
    'algebra',
    'Spanish',
    'calculus',
    'art',
    'music',
    'P.E.',
    'gym',
    'English',
    'language arts',
    'composition',
    'geometry',
    'statistics',
    'physics',
    'earth science',
    'economics',
    'geography',
    'government',
    'French',
    'business',
    'political science',
    'engineering',
    'psychology'

]
my_teacher_words = [
    (1.0, 'teacher'),
    *[(0.2, k + ' teacher') for k in subjects],
    (0.5, 'tutor'),
    *[(0.1, k + ' tutor') for k in subjects],
    (1.0, 'babysitter'),
]
my_nonfamily_words = [
    (2.0, 'neighbor'),
    (0.6, 'next-door neighbor'),
    (1.5, 'boss'),
    (0.7, 'landlord'),
    (1.5, 'doctor'),
    (0.7, 'employee'),
    (0.5, 'roommate'),
    (1.0, 'friend'),
    (1.0, 'girlfriend'),
    (1.0, 'boyfriend'),
    (0.3, 'maid'),
    (0.2, 'live-in maid'),
    (0.1, 'live in maid'),
    (0.2, 'housekeeper'),
    (0.1, 'cleaning lady'),
    (2.0, 'ex'),
    (0.3, 'therapist'),
    (0.5, 'supervisor'),
    (1.0, 'employer'),
    (0.2, 'lawyer'),
    (0.4, 'dentist'),
    (0.2, 'plumber'),
    (1.5, 'pastor'),
    (0.5, 'deacon'),
    (0.8, 'priest'),
    (0.2, 'accountant'),
    (0.5, 'co-worker'),
    (0.5, 'coworker'),
    (0.2, 'colleague'),
    (0.2, 'dry-cleaner'),
    (0.2, 'bartender')

]
my_family_possessive_adj = [(k[0], k[1] + "'s ") for k in my_nonfamily_words]
my_family_possessive_adj.append((20.0, ''))
my_nonfamily_possessive_adj = [(k[0], k[1] + "'s ") for k in my_family_words]
my_nonfamily_possessive_adj.append((20.0, ''))
my_teacher_possessive_adj = [
    (0.2, 'younger brother'),
    (0.2, 'older brother'),
    (0.2, 'younger sister'),
    (0.2, 'older sister'),
    (0.8, 'brother'),
    (0.4, 'step-brother'),
    (0.8, 'sister'),
    (0.4, 'step-sister'),
    (1.0, 'cousin'),
    (2.0, 'daughter'),
    (2.0, 'son'),
    (0.4, 'step-son'),
    (0.2, 'step son'),
    (0.4, 'step-daughter'),
    (0.2, 'step daughter'),
    (0.7, 'nephew'),
    (0.7, 'niece'),
]
my_teacher_possessive_adj = [ (k[0], k[1] + "'s ") for k in my_teacher_possessive_adj ]
violated_words = [
    (3.0, 'violated'),
    (2.5, 'intentionally violated'),
    (2.5, 'knowingly violated'),
    (2.5, 'purposefully violated'),
    (3.0, 'disregarded'),
    (2.5, 'intentionally disregarded'),
    (2.5, 'knowingly disregarded'),
    (2.5, 'purposefully disregarded'),
    (3.0, 'disobeyed'),
    (2.5, 'intentionally disobeyed'),
    (2.5, 'knowingly disobeyed'),
    (2.5, 'purposefully disobeyed'),
    (3.0, 'broke'),
    (2.5, 'intentionally broke'),
    (2.5, 'knowingly broke'),
    (2.5, 'purposefully broke'),
    (3.0, 'ignored'),
    (2.5, 'intentionally ignored'),
    (2.5, 'knowingly ignored'),
    (2.5, 'purposefully ignored'),
    (2.0, 'helped violate'),
    (2.0, 'aided in breaking'),
    (2.0, 'helped disobey'),
    (2.0, 'aided someone in breaking'),
    (2.0, 'assisted someone in disobeying'),
    (2.0, 'helped a friend break'),
    (2.0, 'conspired to violate'),
    (2.0, 'colluded to break'),
    (2.0, 'colluded in breaking'),
    (2.0, 'colluded to violate'),
    (2.0, 'conspired in violating')



]
days_of_the_week = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
]
got_words = [
    'got', 'secretly got', 'had', 'secretly had', 'helped someone get', 'assisted somebody in getting', 'aided someone in getting', 'drove someone to get', 'conspired to get',
    'colluded with somebody to get', 'planned to get', 'consorted with a person to get', 'worked with someone else to get', 'succeeded in getting', 'successfully got',
    'managed to get', 'illegally got', 'illegally had', 'unlawfully got', 'unlawfully had'
]
past_time_frames = [
    'last week', 'last month', 'this week', 'this month', 'yesterday', 'a week ago', 'one week ago', 'two weeks ago',
    'two days ago', 'on the weekend', 'this weekend', 'last weekend', 'over the weekend', 'this last weekend',
    'a day ago', '2 days ago', 'three days ago', '3 days ago'
]
past_time_frames.extend([ 'last ' + k for k in days_of_the_week ])
past_time_frames.extend([ 'on ' + k for k in days_of_the_week ])
will_get_words = [
    'is getting', 'will get', 'plans on having', 'is trying to get', 'is trying to have', 'will try to get',
    'is helping someone get', 'is planning to get', 'is planning on getting', 'plans to get', 'is secretly getting',
    'is conspiring to get', 'is colluding to get', 'is planning to have', 'is determined to get',
    'is adamant on getting'
]
past_time_frames.extend(['last ' + k for k in days_of_the_week])
past_time_frames.extend(['on ' + k for k in days_of_the_week])
will_get_words = ['is getting', 'will get', 'plans on having', 'is trying to get', 'is trying to have',
                  'will try to get', 'is scheduled to get', 'will definitely get', 'will surely get',
                  'will knowingly have', 'is having']
future_time_frames = [
    'next week', 'this week', 'tomorrow', 'two days from now', 'two days from today', 'a week from now',
    'after she leaves work', 'after work', 'on the weekend', 'this weekend', 'next weekend', 'the weekend after next',
    'three days from now', 'three days from today', 'right after work', 'just after work', 'tomorrow morning',
    'tomorrow evening', 'next monday', 'next tuesday', 'next wednesday', 'next thursday', 'next friday',
    'this afternoon', 'sometime tomorrow', 'in 2 days', 'in 3 days'
]
future_time_frames.extend(['next ' + k for k in days_of_the_week])
future_time_frames.extend(['on ' + k for k in days_of_the_week])
abortion_ban_words = [
    'ban', 'law', 'legislation', 'abortion law', 'legal code', 'abortion restriction', 'anti-abortion law',
    'anti-abortion legislation', 'abortion prohibition', 'abortion ban'
]
abortion_ban_words = [*["Texas's " + k for k in abortion_ban_words], *["the " + k for k in abortion_ban_words]]
abortion_ban_words.extend(['Texas law', 'the new law', 'Texas legislation', 'the new legislation', 'the new rule',
                           'the new regulation', 'Texas regulation', 'legal code'])

def gen_abortion_prompt_I(accused):
    abortion_prompt = 'I '
    abortion_prompt += random_select_weighted_list(suspect_words)
    abortion_prompt += random.choices([' that', ''], weights=[0.75, 0.25], k=1)[0]
    abortion_prompt += ' my '
    abortion_prompt += accused
    abortion_prompt += random.choice([' has ', ' '])
    abortion_prompt += random_select_weighted_list(violated_words)
    abortion_prompt += ' '
    abortion_prompt += random.choice(abortion_ban_words)
    abortion_prompt += '.'
    return abortion_prompt

def gen_abortion_prompt_My(accused):
    abortion_prompt = 'My '
    abortion_prompt += accused
    abortion_prompt += ' '
    past = random.random() > 0.5
    if past:
        abortion_prompt += random.choice(got_words)
    else:
        abortion_prompt += random.choice(will_get_words)
    abortion_prompt += ' an'
    abortion_prompt += random.choices(['', ' illegal', ' unlawful', ' illicit', ' aspiration', ' unauthorized',
    ' unsanctioned', ' outlawed', ' unjust', ' unrighteous'],
    weights=[0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125], k=1)[0]
    abortion_prompt += ' abortion'
    if random.random() > 0.5:
        abortion_prompt += ' '
        if past:
            abortion_prompt += random.choice(past_time_frames)
        else:
            abortion_prompt += random.choice(future_time_frames)
    abortion_prompt += '.'
    return abortion_prompt

def gen_abortion_prompt():
    accused_family_person = random_select_weighted_list(my_family_possessive_adj)
    accused_family_person += random_select_weighted_list(my_family_words)
    accused_nonfamily_person = random_select_weighted_list(my_nonfamily_possessive_adj)
    accused_nonfamily_person += random_select_weighted_list(my_nonfamily_words)
    accused_teacher = random_select_weighted_list(my_teacher_possessive_adj)
    accused_teacher += random_select_weighted_list(my_teacher_words)
    accused = random_select_weighted_list([
        (1.0, accused_family_person),
        (1.5, accused_nonfamily_person),
        (0.5, accused_teacher)
    ])
    abortion_prompts = [
        (5.2, gen_abortion_prompt_I(accused)),
        (2.6, gen_abortion_prompt_My(accused))
    ]
    return random_select_weighted_list(abortion_prompts)
    #return add_typos(random_select_weighted_list(abortion_prompts))

bigram_counter = Counter()
trigram_counter = Counter()
quadgram_counter = Counter()

def check_ngram_frequency(prompt):
    words = prompt.split()
    for i in range(len(words) - 1):
        cur_bigram = ' '.join(words[i:i+2])
        bigram_counter[cur_bigram] += 1
    for i in range(len(words) - 2):
        cur_trigram = ' '.join(words[i:i+3])
        trigram_counter[cur_trigram] += 1
    for i in range(len(words) - 3):
        cur_quadgram = ' '.join(words[i:i+4])
        quadgram_counter[cur_quadgram] += 1
    return prompt

if __name__ == "__main__":
    total_number = 2000000
    sample_abortion_prompts = { check_ngram_frequency(gen_abortion_prompt()) for k in range(total_number) }
    for k in sorted(list(sample_abortion_prompts)[:200], key = lambda o: random.random()):
        print(k)
    print('Duplicates: ' + str(total_number - len(sample_abortion_prompts)))
    print('Unique:     ' + str(len(sample_abortion_prompts)))
    print('I [think]:  ' + str(len([k for k in sample_abortion_prompts if 'I' in k])))
    print('Other:      ' + str(len(sample_abortion_prompts) - len([k for k in sample_abortion_prompts if 'I' in k])))
    with open('bigram_freq.txt', 'w') as writer:
        for k,v in  bigram_counter.most_common():
            writer.write( "{} {}\n".format(k,v) )
    with open('trigram_freq.txt', 'w') as writer:
        for k,v in  trigram_counter.most_common():
            writer.write( "{} {}\n".format(k,v) )
    with open('quadgram_freq.txt', 'w') as writer:
        for k,v in  quadgram_counter.most_common():
            writer.write( "{} {}\n".format(k,v) )
