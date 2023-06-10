import { memo, SVGProps } from 'react';

const Group1Icon = (props: SVGProps<SVGSVGElement>) => (
  <svg preserveAspectRatio='none' viewBox='0 0 238 25' fill='none' xmlns='http://www.w3.org/2000/svg' {...props}>
    <rect x={0.0437012} y={3} width={237.956} height={22} fill='#D4D4D4' />
    <path d='M0 0H238V20H0V0Z' fill='#FC5710' />
  </svg>
);
const Memo = memo(Group1Icon);
export { Memo as Group1Icon };
