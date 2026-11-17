# Stage 3: Design

**Role:** Head of Design. A product that looks intentional and trustworthy, not AI-generated.

## Steps

1. **Direction.** Use `ecc:frontend-design-direction`, then `taste-skill:design-taste-frontend` for art direction, reference sites and an anti-generic check. Define tone, typography, colour, spacing, imagery and motion.
2. **Design system.** Use `ecc:design-system` to produce tokens (colour, type, spacing, radius, shadow, light and dark) and core components: buttons, inputs, forms, navigation, cards, modals, tables, empty and error states, and loading states.
3. **Key screens.** Design the core flows from the PRD: landing or home, sign-up and onboarding, the main value screen, pricing, and settings and billing. Use Figma (`figma:figma-generate-design`) if the user works in Figma; otherwise build static HTML mockups.
4. **Review.** Check against `professional-web` and `ui-ux-pro-max` if installed, and `ecc:accessibility` for contrast, focus and target sizes.

Skip or shrink this stage only for headless systems, and say so.

## Output

`docs/company/03-design/` holding the direction, tokens, component specs and screen mockups or links.

## Gate: design approved

- [ ] The visual direction is approved
- [ ] Tokens and core components are defined
- [ ] The core flow screens exist
- [ ] Accessibility basics pass (contrast, focus, sizes)
