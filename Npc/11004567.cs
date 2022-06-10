using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004567: Vasara Chen
/// </summary>
public class _11004567 : NpcScript {
    internal _11004567(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0220211107014547$ 
                // - Really?
                return true;
            case 10:
                // $script:0220211107014548$ 
                // - Hm?
                // $script:0220211107014549$ 
                // - You look strong. Almost as strong as someone I know...
                switch (selection) {
                    // $script:0220211107014550$
                    // - You're one to talk.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0220211107014551$ 
                // - Hey, you ever hear of the Gray Wolf?
                switch (selection) {
                    // $script:0220211107014552$
                    // - I may have heard the name.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0220211107014553$ 
                // - I have a feeling the Gray Wolf will be here. We've got unfinished business...
                return true;
            case 20:
                // $script:0220211107014554$ 
                // - Hey, Gray Wolf.
                switch (selection) {
                    // $script:0220211107014555$
                    // - Vasara Chen?
                    case 0:
                        Id = 21;
                        return false;
                }
                return true;
            case 21:
                // $script:0220211107014556$ 
                // - I knew you'd be here. A fighter like you can't resist the ring for long.
                // $script:0220211107014557$ 
                // - That's why I signed up. Figured it's a good chance for us to duke it out.
                switch (selection) {
                    // $script:0220211107014558$
                    // - This is getting interesting.
                    case 0:
                        Id = 22;
                        return false;
                }
                return true;
            case 22:
                // $script:0220211107014559$ 
                // - I hope you haven't slacked off in your training. I haven't.
                return true;
            default:
                return true;
        }
    }
}
