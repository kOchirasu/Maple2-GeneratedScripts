using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003126: 
/// </summary>
public class _11003126 : NpcScript {
    internal _11003126(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0131151207007897$ 
                // - Good to see you, $MyPCName$!
                return true;
            case 30:
                // $script:0131151207007900$ 
                // - Hey there, $MyPCName$. How would you like to decorate and share your creations to your heart's content? There's a place for that, and it's called Builder's Park!
                switch (selection) {
                    // $script:0131151207007901$
                    // - I don't think so.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0131151207007902$
                    // - I like the sound of that!
                    case 1:
                        Id = 33;
                        return false;
                }
                return true;
            case 31:
                // $script:0131151207007903$ 
                // - Hmm, maybe you should let me explain first. It all started with a freak waterspout in the middle of the open sea. When the water finally calmed, a new island appeared in its wake.
                // $script:0131151207007904$ 
                // - The palace officially named the land Vanica, but designated it a place for anyone to come and build whatever they want. People started calling it Builder's Park, since they could just build houses and decorate the land with no limits. $MyPCName$, how'd you like to check it out and meet some new friends?
                switch (selection) {
                    // $script:0131151207007905$
                    // - How can I get to Vanica?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0131151207007906$ 
                // - Easy! Just enter this oh-so-convenient portal next to me, and next thing you know you'll be in $map:02000407$, right in the heart of Vanica.
                return true;
            case 33:
                // $script:0131151207007907$ 
                // - Oh, really? So, you've already built and decorated to your hear's content?
                switch (selection) {
                    // $script:0131151207007908$
                    // - Yep!
                    case 0:
                        Id = 34;
                        return false;
                    // $script:0131151207007909$
                    // - Nope!
                    case 1:
                        Id = 35;
                        return false;
                }
                return true;
            case 34:
                // $script:0131151207007910$ 
                // - Wow $MyPCName$, you get around! It really is more fun to build with others than to do it on your own, right? Be sure to head back to Vanica whenever you want to make some new memories together.
                return true;
            case 35:
                // $script:0131151207007911$ 
                // - Well then, let me explain how to get there! Are you ready? Okay, step one is to enter this portal next to me. That's it! It'll take you straight to $map:02000407$, in the heart of Vanica.
                return true;
            default:
                return true;
        }
    }
}
