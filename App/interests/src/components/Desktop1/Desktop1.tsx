import { memo } from 'react';
import type { FC } from 'react';

import resets from '../_resets.module.css';
import { Component1_StateChecked } from './Component1_StateChecked/Component1_StateChecked';
import { Component1_StateDefault } from './Component1_StateDefault/Component1_StateDefault';
import classes from './Desktop1.module.css';
import { Group1Icon } from './Group1Icon';
import { VectorIcon } from './VectorIcon';
import { VectorIcon2 } from './VectorIcon2';

interface Props {
  className?: string;
}
/* @figmaId 267:42 */
export const Desktop1: FC<Props> = memo(function Desktop1(props = {}) {
  return (
    <div className={`${resets.storybrainResets} ${classes.root}`}>
      <div className={classes.vector8}>
        <VectorIcon className={classes.icon} />
      </div>
      <div className={classes.home}>Home</div>
      <div className={classes.vector9}>
        <VectorIcon2 className={classes.icon2} />
      </div>
      <div className={classes.royalGalaxy}>Royal Galaxy</div>
      <div className={classes.blueMoonHotel}>Blue Moon Hotel</div>
      <div className={classes.distance12km}>Distance 1.2km</div>
      <div className={classes.group1}>
        <Group1Icon className={classes.icon3} />
      </div>
      <div className={classes.tellUsAboutYourInterestsToGive}>
        <div className={classes.textBlock}>Tell us about your interests to give more accurate matches!</div>
        <div className={classes.textBlock2}>
          <p></p>
        </div>
        <div className={classes.textBlock3}>Please indicate at least one interest</div>
      </div>
      <div className={classes.adventure}>Adventure</div>
      <div className={classes.history}>History</div>
      <div className={classes.nature}>Nature</div>
      <div className={classes.food}>Food</div>
      <div className={classes.shopping}>Shopping</div>
      <div className={classes.beach}>Beach</div>
      <div className={classes.nightlife}>Nightlife</div>
      <div className={classes.image1}></div>
      <Component1_StateDefault className={classes.component1} classes={{ vector: classes.vector }} />
      <div className={classes.image2}></div>
      <div className={classes.image3}></div>
      <div className={classes.image4}></div>
      <div className={classes.image5}></div>
      <Component1_StateDefault className={classes.component12} classes={{ vector: classes.vector2 }} />
      <Component1_StateDefault className={classes.component13} classes={{ vector: classes.vector3 }} />
      <Component1_StateDefault className={classes.component14} classes={{ vector: classes.vector4 }} />
      <Component1_StateChecked className={classes.component15} />
      <Component1_StateDefault className={classes.component16} classes={{ vector: classes.vector5 }} />
      <Component1_StateDefault className={classes.component17} classes={{ vector: classes.vector6 }} />
      <Component1_StateDefault className={classes.component18} classes={{ vector: classes.vector7 }} />
      <div className={classes.image6}></div>
      <div className={classes.image7}></div>
    </div>
  );
});
