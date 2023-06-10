import { memo } from 'react';
import type { FC } from 'react';

import resets from '../../_resets.module.css';
import classes from './SearchResultsForBali.module.css';

interface Props {
  className?: string;
}
/* @figmaId 207:111 */
export const SearchResultsForBali: FC<Props> = memo(function SearchResultsForBali(props = {}) {
  return <div className={`${resets.storybrainResets} ${classes.root}`}></div>;
});
