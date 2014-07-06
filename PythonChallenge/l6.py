"""
Using the zipfile module to interact with Zip files. Can do all the *usual* zip
operations, as well as get at the metadata. The zipfile module obviously
transparently opens the file as well - as we can use the *with* syntax.

Can solve this using regex patterns too as depicted before, but this worked, so
I didn't try it that way this time.

Also demonstrates basic usage of a dict() in Python, although this is pretty
standard - the way everyone already uses it.
"""
import zipfile

def main():
    all_comments = {}
    comment = ""

    with zipfile.ZipFile('l6_channel.zip', 'r') as myzip:
        memberinfo = myzip.infolist()
        for m1 in memberinfo:
            content = myzip.read(m1).split()[-1]
            comment = m1.comment
            filename = m1.filename
            all_comments[filename] = content+'^'+comment

    t1 = all_comments['90052.txt'].split('^')
    next_nothing = t1[0]
    comment += t1[1]

    for count in range(len(all_comments)):
        if not next_nothing.startswith('comments'):
            t1 = all_comments[str(next_nothing)+'.txt'].split('^')
            next_nothing = t1[0]
            comment += t1[1]

    print comment

if __name__ == "__main__":
    main()
