import { memo } from 'react';
import type { FC } from 'react';

import resets from '../_resets.module.css';
import classes from './Desktop1.module.css';
import { Line1Icon } from './Line1Icon.js';
import { VectorIcon2 } from './VectorIcon2.js';
import { VectorIcon3 } from './VectorIcon3.js';
import { VectorIcon4 } from './VectorIcon4.js';
import { VectorIcon5 } from './VectorIcon5.js';
import { VectorIcon6 } from './VectorIcon6.js';
import { VectorIcon7 } from './VectorIcon7.js';
import { VectorIcon8 } from './VectorIcon8.js';
import { VectorIcon9 } from './VectorIcon9.js';
import { VectorIcon } from './VectorIcon.js';

interface Props {
  className?: string;
}
/* @figmaId 101:3 */
export const Desktop1: FC<Props> = memo(function Desktop1(props = {}) {
  return (
    <div className={`${resets.storybrainResets} ${classes.root}`}>
      <div className={classes.rectangle1}></div>
      <div className={classes.aUniqueExperienceWhereYouMeetN}>
        a unique experience where you meet new people and travel together{' '}
      </div>
      <div className={classes.getReady}>Get ready....</div>
      <div className={classes.rectangle2}></div>
      <div className={classes.login}>Login</div>
      <div className={classes.rectangle22}></div>
      <div className={classes.signUp}>Sign Up</div>
      <div className={classes.vector}>
        <VectorIcon className={classes.icon} />
      </div>
      <div className={classes.vector2}>
        <VectorIcon2 className={classes.icon2} />
      </div>
      <div className={classes.line1}>
        <Line1Icon className={classes.icon3} />
      </div>
      <div className={classes.vector3}>
        <VectorIcon3 className={classes.icon4} />
      </div>
      <div className={classes.discounts}>Discounts</div>
      <div className={classes.discover}>Discover</div>
      <div className={classes.places}>Places</div>
      <div className={classes.housing}>Housing</div>
      <div className={classes.home}>Home</div>
      <div className={classes.search}>Search</div>
      <div className={classes.seeAll}>See all</div>
      <div className={classes.rectangle5}></div>
      <div className={classes.vector4}>
        <VectorIcon4 className={classes.icon5} />
      </div>
      <div className={classes.rectangle6}></div>
      <div className={classes.rectangle7}></div>
      <div className={classes.rectangle8}></div>
      <div className={classes.rectangle9}></div>
      <div className={classes.vector5}>
        <VectorIcon5 className={classes.icon6} />
      </div>
      <div className={classes.vector6}>
        <VectorIcon6 className={classes.icon7} />
      </div>
      <div className={classes.vector7}>
        <VectorIcon7 className={classes.icon8} />
      </div>
      <div className={classes.vector8}>
        <VectorIcon8 className={classes.icon9} />
      </div>
      <div className={classes.vector9}>
        <VectorIcon9 className={classes.icon10} />
      </div>
      <div className={classes.royalGalaxy}>Royal Galaxy</div>
      <div className={classes.blueMoonHotel}>Blue Moon Hotel</div>
      <div className={classes.redVelvetInn}>Red Velvet Inn</div>
      <div className={classes.distance12km}>Distance 1.2km</div>
      <div className={classes.distance12km2}>Distance 1.2km</div>
      <div className={classes.distance12km3}>Distance 1.2km</div>
      <div className={classes.people}>People</div>
      <div className={classes.frame1}></div>
    </div>
  );
});
