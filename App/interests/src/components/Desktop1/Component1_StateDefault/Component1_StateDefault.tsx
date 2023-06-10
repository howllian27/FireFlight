import { memo } from 'react';
import type { FC } from 'react';

import resets from '../../_resets.module.css';
import classes from './Component1_StateDefault.module.css';

interface Props {
  className?: string;
  classes?: {
    vector?: string;
    root?: string;
  };
}
/* @figmaId 256:31 */
export const Component1_StateDefault: FC<Props> = memo(function Component1_StateDefault(props = {}) {
  return (
    <div
      className={`${resets.storybrainResets} ${props.classes?.root || ''} ${props.className || ''} ${classes.root}`}
    ></div>
  );
});
