from app import db
from app.models import Assessment

# Initialise list of assessments
assessments = list()

# Add a bunch of assessments
assessments.append(Assessment(
    question="""If a person running with an inital speed of 5m/s slows down
with an acceleration of 0.5m/s^2,
how long does it take for them to stop moving/ have a final speed of 0. Do not put units in your answer.""", 
    answer="10"))


assessments.append(Assessment(
    question="""If a cat had an initial velocity 3m/s,
speeds up with an acceleration of 1 m/s^2, and travels 10m,
what is its final velocity at the end of the 10 meters?
Do not put units in your answer, use 3 decimal places in your answer.""", 
    answer="5.385"))

assessments.append(Assessment(
    question="""If a comet has an initial velocity 1000m/s,
and has a final velocity of 3000m/s,
if there was 30 seconds between the comet having the intial speed and the final speed,
how far did it travel? Do not put units in your answer.""", 
    answer="60000"))

assessments.append(Assessment(
    question="""If a car had an initial velocity 10m/s,
speeds up with an acceleration of 1 m/s^2 for 10 seconds
how far did it travel? Do not put units in your answer.""", 
    answer="150"))


assessments.append(Assessment(
    question="""If a peregrine falcon dives with a final velocity 90m/s,
if it started at rest(with a initial velocity of 0m/s),
if it took 3 seconds to go from rest to final velocity,
what was its acceleration? Do not put units in your answer.""", 
    answer="30"))

assessments.append(Assessment(
    question="""If a ball rolls down a hill with an initial speed of 3m/s,
if at the end of its journey it has a velocity of 5m/s,
if the ball was rolling for 10 seconds,
how far did it travel? Do not put units in your answer.""", 
    answer="40"))

assessments.append(Assessment(
    question="""If a spaceship is travelling with a final velocity of 1000m/s
after accelerating at 20m/s^2 for 10 seconds,
what was its velocity before travelling? Do not put units in your answer.""", 
    answer="800"))

# Add the list to the database
for assessment in assessments:
    db.session.add(assessment)
db.session.commit()