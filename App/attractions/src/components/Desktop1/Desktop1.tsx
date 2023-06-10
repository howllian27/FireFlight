import { memo } from 'react';
import type { FC } from 'react';

import resets from '../_resets.module.css';
import classes from './Desktop1.module.css';
import { Group1Icon } from './Group1Icon.js';
import { SearchResultsForBali } from './SearchResultsForBali/SearchResultsForBali';
import { VectorIcon2 } from './VectorIcon2.js';
import { VectorIcon3 } from './VectorIcon3.js';
import { VectorIcon4 } from './VectorIcon4.js';
import { VectorIcon5 } from './VectorIcon5.js';
import { VectorIcon6 } from './VectorIcon6.js';
import { VectorIcon7 } from './VectorIcon7.js';
import { VectorIcon } from './VectorIcon.js';

interface Props {
  className?: string;
}
/* @figmaId 204:3 */
export const Desktop1: FC<Props> = memo(function Desktop1(props = {}) {
  return (
    <div className={`${resets.storybrainResets} ${classes.root}`}>
      <div className={classes.places}>Places</div>
      <div className={classes._1}>01</div>
      <div className={classes._3}>03</div>
      <div className={classes.group1}>
        <Group1Icon className={classes.icon} />
      </div>
      <div className={classes.vector}>
        <VectorIcon className={classes.icon2} />
      </div>
      <div className={classes.vector2}>
        <VectorIcon2 className={classes.icon3} />
      </div>
      <div className={classes.home}>Home</div>
      <div className={classes.royalGalaxy}>Royal Galaxy</div>
      <div className={classes.redVelvetInn}>Red Velvet Inn</div>
      <div className={classes.distance12km}>Distance 1.2km</div>
      <div className={classes.distance12km2}>Distance 1.2km</div>
      <SearchResultsForBali />
      <div className={classes.searchResultsForBali}>Search Results for Bali</div>
      <div className={classes.rectangle7}></div>
      <div className={classes.rectangle8}></div>
      <div className={classes.nungWaterFall}>Nung WaterFall</div>
      <div className={classes.rectangle9}></div>
      <div className={classes.distance12km3}>Distance 1.2km</div>
      <div className={classes.greenBowlBeach}>Green Bowl Beach</div>
      <div className={classes.rectangle10}></div>
      <div className={classes.subakMuseum}>Subak Museum</div>
      <div className={classes.rectangle11}></div>
      <div className={classes.frame1}>
        <div className={classes.artMarket}>Art Market</div>
      </div>
      <div className={classes.mountBatur}>Mount Batur</div>
      <div className={classes.filter}>Filter</div>
      <div className={classes.distance12km4}>Distance 1.2km</div>
      <div className={classes.distance12km5}>Distance 1.2km</div>
      <div className={classes.vector3}>
        <VectorIcon3 className={classes.icon4} />
      </div>
      <div className={classes.vector4}>
        <VectorIcon4 className={classes.icon5} />
      </div>
      <div className={classes.vector5}>
        <VectorIcon5 className={classes.icon6} />
      </div>
      <div className={classes.vector6}>
        <VectorIcon6 className={classes.icon7} />
      </div>
      <div className={classes.vector7}>
        <VectorIcon7 className={classes.icon8} />
      </div>
    </div>
  );
});
