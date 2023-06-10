import { memo, SVGProps } from 'react';

const VectorIcon = (props: SVGProps<SVGSVGElement>) => (
  <svg preserveAspectRatio='none' viewBox='0 0 34 24' fill='none' xmlns='http://www.w3.org/2000/svg' {...props}>
    <path d='M11.9 23.7L0.7 12.5L2.85 10.35L11.9 19.4L31.1 0.2L33.25 2.35L11.9 23.7Z' fill='white' />
  </svg>
);
const Memo = memo(VectorIcon);
export { Memo as VectorIcon };
