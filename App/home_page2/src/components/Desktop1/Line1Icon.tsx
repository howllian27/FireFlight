import { memo, SVGProps } from 'react';

const Line1Icon = (props: SVGProps<SVGSVGElement>) => (
  <svg preserveAspectRatio='none' viewBox='0 0 365 434' fill='none' xmlns='http://www.w3.org/2000/svg' {...props}>
    <path
      d='M81.9539 2.77637C81.9539 2.77637 66.7036 181.28 179.892 178.929C309.192 176.244 278.954 433.325 278.954 433.325'
      stroke='white'
      strokeWidth={4}
      strokeLinecap='square'
      strokeDasharray='10 10'
    />
  </svg>
);
const Memo = memo(Line1Icon);
export { Memo as Line1Icon };
