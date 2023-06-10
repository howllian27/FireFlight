import { memo, SVGProps } from 'react';

const Group1Icon = (props: SVGProps<SVGSVGElement>) => (
  <svg preserveAspectRatio='none' viewBox='0 0 238 27' fill='none' xmlns='http://www.w3.org/2000/svg' {...props}>
    <rect x={0.0436707} y={3} width={237.956} height={22} fill='#D4D4D4' />
    <path d='M-3.05176e-05 0H90V27H-3.05176e-05V0Z' fill='#FC5710' />
  </svg>
);
const Memo = memo(Group1Icon);
export { Memo as Group1Icon };
