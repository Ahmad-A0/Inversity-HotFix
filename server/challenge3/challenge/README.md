# *Log4Jelly: A Wobbly Situation at JelloFresh*

Welcome, brave code warrior, to the jiggly world of JelloFresh, where desserts are serious business and logging is... well, let's just say it's a bit shaky.

## The Sticky Situation

JelloFresh, the world's premier online jelly and pudding delivery service, has a problem. Their logging system, affectionately named Log4Jelly, is about as stable as a tower of jelly cubes in an earthquake. Why, you ask? Well, some genius thought it would be a great idea to use `eval()` in their logger. Yep, you heard that right - they're basically inviting hackers to have a jelly party in their systems!

## Your Wobbly Mission

As JelloFresh's newly hired "Gelatin Security Specialist" (yes, that's a real title now), your task is to save the company from turning into a hacker's trifle. Here's what you need to do:

1. SSH into the JelloFresh server (careful, the keys are a bit slippery).
2. Navigate to the `/app` directory (watch your step, there's spilled jelly everywhere).
3. Open `app.js` in your favorite text editor (we recommend Vim for extra jiggle).
4. Locate the `logger` function - it should be the one that looks like it was written by a sugar-high five-year-old.
5. Remove the unsafe `eval()` call. Remember, `eval()` is like adding a "kick me" sign to your code.
6. Refactor the logger to be less... wobbly. Make it stable, secure, and jelly-proof!
7. Ensure it still logs all the important stuff - we need to know when we're running low on gelatin, after all.

## Hints for the Jelly-Brained

- `eval()` is not your friend. It's the guy who shows up uninvited to your jelly party and eats all the good flavors.
- Try using template literals or good old string concatenation. They're like the sturdy bowls of the coding world.
- Keep the log levels intact. We need to know the difference between a "the jelly's too jiggly" warning and a "the pudding is on fire" error.

## Submitting Your Jelly-tastic Solution

Once you've successfully de-wobbled the logger:

1. Save your changes to `app.js`. Don't worry, the 'save' button isn't made of jelly.
2. Exit the text editor (try not to get stuck).
3. Our state-of-the-art Jelly-AI will automatically detect and evaluate your changes.

Remember, the fate of JelloFresh rests in your hands. No pressure, but if you fail, millions will be deprived of their daily jelly fix. We believe in you, oh mighty Gelatin Guru!

Now go forth and make Log4Jelly as solid as... well, not jelly, but you get the idea!
