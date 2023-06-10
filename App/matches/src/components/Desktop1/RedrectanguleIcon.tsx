import { memo, SVGProps } from 'react';

const RedrectanguleIcon = (props: SVGProps<SVGSVGElement>) => (
  <svg preserveAspectRatio='none' viewBox='0 0 282 776' fill='none' xmlns='http://www.w3.org/2000/svg' {...props}>
    <path
      d='M0 25C0 11.1929 11.1929 0 25 0H257C270.807 0 282 11.1929 282 25V751C282 764.807 270.807 776 257 776H25C11.1929 776 0 764.807 0 751V25Z'
      fill='#B93E45'
    />
  </svg>
);
const Memo = memo(RedrectanguleIcon);
export { Memo as RedrectanguleIcon };
