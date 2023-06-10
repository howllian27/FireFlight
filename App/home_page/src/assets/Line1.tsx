export default function Line1(props: Line1Props) {
  return (
    <div className={`${props.className}`}>
      <svg
        width="100%"
        height="100%"
        preserveAspectRatio="none"
        viewBox="0 0 206 436"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M 2.954 2.776 C 2.954 2.776 -12.296 181.28 100.892 178.929 C 230.192 176.244 199.954 433.325 199.954 433.325"
          stroke="white"
          strokeWidth="4"
          strokeLinecap="square"
          strokeDasharray="10 10"
         />
      </svg>
    </div>
  );
}

Line1.defaultProps = {
  className: "",
};

interface Line1Props {
  className: string;
}

/**
 * This component was generated from Figma with FireJet.
 * Learn more at https://www.firejet.io
 *
 * README:
 * The output code may look slightly different when copied to your codebase. To fix this:
 * 1. Include the necessary fonts. The required fonts are imported from public/index.html
 * 2. Include the global styles. They can be found in App.css
 *
 * Note: Step 2 is not required for tailwind.css output
 */
