import { memo } from 'react';
import type { FC } from 'react';

import resets from '../_resets.module.css';
import classes from './Desktop1.module.css';
import { FriendsIcon } from './FriendsIcon.js';
import { Group1Icon } from './Group1Icon.js';
import { RedrectanguleIcon } from './RedrectanguleIcon.js';
import { VectorIcon2 } from './VectorIcon2.js';
import { VectorIcon3 } from './VectorIcon3.js';
import { VectorIcon } from './VectorIcon.js';

interface Props {
  className?: string;
}
/* @figmaId 206:53 */
export const Desktop1: FC<Props> = memo(function Desktop1(props = {}) {
  return (
    <div className={`${resets.storybrainResets} ${classes.root}`}>
      <div className={classes.vector}>
        <VectorIcon className={classes.icon} />
      </div>
      <div className={classes.home}>Home</div>
      <div className={classes.filter}>Filter</div>
      <div className={classes.vector2}>
        <VectorIcon2 className={classes.icon2} />
      </div>
      <div className={classes.royalGalaxy}>Royal Galaxy</div>
      <div className={classes.blueMoonHotel}>Blue Moon Hotel</div>
      <div className={classes.distance12km}>Distance 1.2km</div>
      <div className={classes.distance12km2}>Distance 1.2km</div>
      <div className={classes.rEDRECTANGULE}>
        <RedrectanguleIcon className={classes.icon3} />
      </div>
      <div className={classes.profiles}>Profiles</div>
      <div className={classes._10K}>10K</div>
      <div className={classes.matchesYourInterest}>Matches your interest</div>
      <div className={classes._641}>641</div>
      <div className={classes.interestedInYou}>Interested in you</div>
      <div className={classes._21k}>2.1k</div>
      <div className={classes.line2}></div>
      <div className={classes.line1}></div>
      <div className={classes.fRIENDS}>
        <FriendsIcon className={classes.icon4} />
      </div>
      <div className={classes.topResults}>Top Results</div>
      <div className={classes.diana}>Diana</div>
      <div className={classes.leon}>Leon</div>
      <div className={classes.daisy}>Daisy</div>
      <div className={classes.james}>James</div>
      <div className={classes.fiona}>Fiona</div>
      <div className={classes._1}>01</div>
      <div className={classes.group1}>
        <Group1Icon className={classes.icon5} />
      </div>
      <div className={classes._21}>21</div>
      <div className={classes.vector3}>
        <VectorIcon3 className={classes.icon6} />
      </div>
      <div className={classes.rectangle2}></div>
      <div className={classes.follow}>Follow</div>
      <div className={classes.rectangle22}></div>
      <div className={classes.follow2}>Follow</div>
      <div className={classes.rectangle23}></div>
      <div className={classes.follow3}>Follow</div>
      <div className={classes.rectangle24}></div>
      <div className={classes.follow4}>Follow</div>
      <div className={classes.rectangle25}></div>
      <div className={classes.follow5}>Follow</div>
      <div className={classes.travelWebsiteTemplate}></div>
    </div>
  );
});
