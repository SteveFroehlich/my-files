# Relationship management system


## Schema
```
people/
  people-index.csv
  _templates/
    person-snapshot-template.md
    person-interaction-template.md

  jane-doe/
    jane-doe-snapshot.md
    interactions/
      2026-05-15-in-person-jane-doe.md
      2026-06-15-text-jane-doe.md

  alex-smith/
    alex-smith-snapshot.md
    interactions/
      2026-05-20-video-call-alex-smith.md
```

## Descriptions
`people-index.csv` answers the question what relationship should I invest energy in for the coming week?

Each person gets a directory.

`interactions` directory holds a file for each interaction.

## Enums

#### interaction .md file
**interaction_type**
* email
* text
* video-call
* phone-call
* in-person
* group-event

#### snapshot .md file 
placeholder

#### people-index.csv
**status**
* in_circle
* engaged
* following
* dormant

**category** 
* colleague

**target_frequency**
* as-needed