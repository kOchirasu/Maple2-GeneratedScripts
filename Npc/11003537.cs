using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003537: Mason
/// </summary>
public class _11003537 : NpcScript {
    internal _11003537(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1126150707011943$ 
                // - It is time my order stood with the rest of the empire. 
                return true;
            case 20:
                // $script:1126150707011944$ 
                // - I'm listening. 
                switch (selection) {
                    // $script:1126150707011945$
                    // - What are the Lumiknights, exactly?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1126150707011946$ 
                // - The existence of the Lumiknights may no longer be a secret, but that doesn't mean I may speak freely of what we do. In accordance to the Pact of Dantalion, my tongue is bound. 
                switch (selection) {
                    // $script:1126150707011947$
                    // - Your what is huh?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1126150707011948$ 
                // - Of course, if you apply the Third Law of the Equinox, I suppose it wouldn't hurt to let slip a word or two. So long as you remember your Rites of Obfuscation, of course. 
                switch (selection) {
                    // $script:1126150707011949$
                    // - Of... of course...
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:1126150707011950$ 
                // - You can't take these things too lightly. I once spoke the Three Devastating Truths to an insuitably prepared koborc, and it inverted into a quasi-nonsubstantiated autoform. Ha-ha! 
                switch (selection) {
                    // $script:1126150707011951$
                    // - Is that... funny...?
                    case 0:
                        Id = 34;
                        return false;
                }
                return true;
            case 34:
                // $script:1126150707011952$ 
                // - You don't think so? I suppose my sense of humor is more sophisticated than most. 
                switch (selection) {
                    // $script:1126150707011953$
                    // - Anyway, about the Lumiknights?
                    case 0:
                        Id = 35;
                        return false;
                }
                return true;
            case 35:
                // $script:1126150707011954$ 
                // - Before you can even begin to comprehend the Lumiknights, you must open your mind to the myriad possibilities of the universe. It can take years of study. Shall we begin with a light reading of the Tome of Bombastic Insensations? 
                switch (selection) {
                    // $script:1126150707011955$
                    // - You know what? Never mind.
                    case 0:
                        Id = 36;
                        return false;
                }
                return true;
            case 36:
                // $script:1126150707011956$ 
                // - How unfortunate. Well, if you change your mind, you know where to find me. 
                return true;
            case 40:
                // $script:1126150707011957$ 
                // - You are not prepared. 
                return true;
            default:
                return true;
        }
    }
}
