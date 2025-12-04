
# Contact Book

Manage your contacts - add, search & delete.

## Installation

```bash
pip install git+https://github.com/shubham-kv/mini-python-projects.git#egg=contact_book\&subdirectory=04-contact-book
```

## Usage

```bash
$ contacts add "John" --email "john@email.com" --phone "+(720) 555-3390"
$ contacts add "Joanne" --email "joanne@email.com" --phone "+(720) 555-8772"
$ contacts add "Michael" --email "michael@email.com" --phone "+(512) 555-2104"
$ contacts add "Michelle" --email "michelle@email.com" --phone "+(512) 555-1284"

$ contacts list
Id                         | Name                 | Phone           | Email
01KBMTXMR1R6SDHQV9XY4FV82M | John                 | +(720) 555-3390 | john@email.com
01KBMTXX3YTJWNNPSSY31Z70BN | Joanne               | +(720) 555-8772 | joanne@email.com
01KBMTY4PZGCEA70FVPBBQHNY7 | Michael              | +(512) 555-2104 | michael@email.com
01KBMTYBCXRV3ZTYRT2GZ2JZ1Z | Michelle             | +(512) 555-1284 | michelle@email.com

$ contacts search jo
Id                         | Name                 | Phone           | Email
01KBMTXMR1R6SDHQV9XY4FV82M | John                 | +(720) 555-3390 | john@email.com
01KBMTXX3YTJWNNPSSY31Z70BN | Joanne               | +(720) 555-8772 | joanne@email.com

$ contacts delete 01KBMTYBCXRV3ZTYRT2GZ2JZ1Z
Contact Deleted!

$ contacts delete 01KBMTY4PZGCEA70FVPBBQHNY7
Contact Deleted!

$ contacts list
Id                         | Name                 | Phone           | Email
01KBMTXMR1R6SDHQV9XY4FV82M | John                 | +(720) 555-3390 | john@email.com
01KBMTXX3YTJWNNPSSY31Z70BN | Joanne               | +(720) 555-8772 | joanne@email.com
```

## LICENSE

MIT
