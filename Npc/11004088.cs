using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004088: Rainsong Fairy
/// </summary>
public class _11004088 : NpcScript {
    internal _11004088(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0622133907010301$ 
                // - A cold and rainy day, like when we met.
                //   His eyes, his love, I never will forget...
                return true;
            case 10:
                // $script:0622133907010302$ 
                // - A cold and rainy day, like when we met.
                //   His eyes, his love, I never will forget...
                // $script:0622133907010303$ 
                // - I see a wand'rer, hail! Be welcome here.
                //   This is Ellosylva, the Fairy's Tear.
                switch (selection) {
                    // $script:0622133907010304$
                    // - That's a sad name.
                    case 0:
                        Id = 31;
                        return false;
                }
                // $script:0625134307010363$ 
                // - Once a fairy falls in love, she never forgets her lover, even after they've gone to the place where we cannot follow...
                // $script:0625134307010364$ 
                // - I broke the rules and fell in love. I first met him here in $map:02000042$. It still smells like him...
                // $script:0625134307010365$ 
                // - We were happy together, but it couldn't last. And now, I can never see him again...
                // $script:0622133907010309$ 
                // - He told me that my song made him think of the rain. That is why I sing here—to remember him. But, no matter how cheerfully I try to sing, it always comes out sad...
                switch (selection) {
                    // $script:0625134307010366$
                    // - It's a beautiful song.
                    case 0:
                        Id = 37;
                        return false;
                }
                return true;
            case 31:
                // $script:0622133907010305$ 
                // - We fairies oft wear smiles bright and hale,
                //   but in this rain, I share my pain, my tale.
                switch (selection) {
                    // $script:0622133907010306$
                    // - What's your story?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0622133907010308$ 
                // - A human's heart I held in hand, and mine
                //   in his. But human lives are short and I
                //   was left behind when it came to be his time.
                return true;
            case 37:
                // $script:0625134307010367$ 
                // - Thank you, traveler. I like to think that he's out there, somewhere, still listening to me. Come see me again whenever you want to hear me sing.
                return true;
            default:
                return true;
        }
    }
}
