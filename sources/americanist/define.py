import csv
from pyclts import CLTS
clts = CLTS('/mnt/c/Github/clts/')
napa = clts.transcriptionsystem('napa')
asjp = clts.transcriptionsystem('asjpcode')
snd1 = clts.bipa['ts']
stringer = napa.translate('ʠ w à ʔ ṣ̌ o ʔ t á l e', clts.bipa)
snd1.name
firstRound = True

with open('americanist-source.tsv', 'r', encoding='utf-8') as tsvfile:
    with open('americanist.tsv', 'w', encoding='utf-8') as out_file:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        tsv_writer = csv.writer(out_file, delimiter='\t')
        charClass = ""
        for row in reader:
            tempClass = row['BIPA']
            if row['BIPA'].startswith("#"):
                charClass = row['BIPA'][1:]
                # This is Tempoarary
                # tsv_writer.writerow(row['BIPA'])
            else:
                ipa = row['BIPA']
                row['Description'] = clts.bipa[ipa].name
                row['Dataset'] = "americanist"
                if (row['BIPA'] == row['Americanist']):
                    row['Change'] = 0
                else:
                    row['Change'] = 1
                row['Class'] = charClass
                print(row)
                keys, values = [], []
                for key, value in row.items():
                    keys.append(key)
                    values.append(value)
                if firstRound:
                    tsv_writer.writerow(keys)
                    firstRound = False
                tsv_writer.writerow(values)
firstRound = True
with open('americanist.tsv', 'r', encoding='utf-8') as sourcy:
    reader = csv.DictReader(sourcy, dialect='excel-tab')
    with open('/mnt/c/Github/clts/pkg/transcriptionsystems/americanist/consonants-a.tsv', 'w', encoding='utf-8') as consonant_file:
        consonant_writer = csv.writer(consonant_file, delimiter='\t')
        for row in reader:
            descrip = row['Description'].split(" ")

            if "consonant" in row['Description']:
                if firstRound:
                    consonant_writer.writerow(
                        ['GRAPHEME', 'PHONATION', 'PLACE', 'MANNER', 'ALIAS', 'EXTRA', 'NOTE'])
                    firstRound = False
                # print(row['Description'])
                consonant_writer.writerow(
                    [row['Americanist'], descrip[0], descrip[1], descrip[2], '', 'Matthew', row['Note']])
