import { memo } from 'react';
import type { FC } from 'react';

import resets from '../_resets.module.css';
import classes from './Desktop1.module.css';
import { Group1Icon } from './Group1Icon';
import { VectorIcon } from './VectorIcon';
import { VectorIcon2 } from './VectorIcon2';

interface Props {
  className?: string;
}
/* @figmaId 265:7 */
export const Desktop1: FC<Props> = memo(function Desktop1(props = {}) {
  return (
    <div className={`${resets.storybrainResets} ${classes.root}`}>
      <div className={classes.vector}>
        <VectorIcon className={classes.icon} />
      </div>
      <div className={classes.home}>Home</div>
      <div className={classes._1}>01</div>
      <div className={classes.group1}>
        <Group1Icon className={classes.icon2} />
      </div>
      <div className={classes._2}>02</div>
      <div className={classes.vector2}>
        <VectorIcon2 className={classes.icon3} />
      </div>
      <div className={classes.macaron_bg}></div>
      <div className={classes.jamieBrownWm4DuvIpLj8Unsplash1}></div>
      <div className={classes.setProfilePicture}>Set Profile Picture</div>
      <div className={classes.enterDetails}>Enter details</div>
      <div className={classes.rectangle6}></div>
      <div className={classes.password}>Password</div>
      <div className={classes.unnamed}>*****************</div>
      <div className={classes.rectangle62}></div>
      <div className={classes.aboutMe}>About me</div>
      <div className={classes.loveCookingBakeryAddictCulinar}>
        <div className={classes.textBlock}>Love cooking | Bakery addict</div>
        <div className={classes.textBlock2}>Culinary blogger</div>
      </div>
      <div className={classes.rectangle4}></div>
      <div className={classes.username}>Username</div>
      <div className={classes.ivanaYummyfoodies}>Ivana.yummyfoodies</div>
      <div className={classes.rectangle3}></div>
      <div className={classes.fullName}>Full Name</div>
      <div className={classes.ivanaKiara}>Ivana Kiara</div>
      <div className={classes.rectangle2}></div>
      <div className={classes.email}>Email</div>
      <div className={classes.ivanaKiaraGmailCom}>Ivana.kiara@gmail.com</div>
    </div>
  );
});
