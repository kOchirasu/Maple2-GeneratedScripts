using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004483: Cabomba
/// </summary>
public class _11004483 : NpcScript {
    internal _11004483(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012249$ 
                // - Hello! I'll be helping you explore Kritias. Nice to meet you.
                return true;
            case 10:
                // $script:1227192907012250$ 
                // - Hello! I'll be helping you explore Kritias. Nice to meet you.
                switch (selection) {
                    // $script:1227192907012251$
                    // - When do you start?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012252$ 
                // - St-st-st-start? Soon! Really soon! Yeah...
                // $script:1227192907012253$ 
                // - There's lots and lots of preparation to do. So that's what I'm doing... Preparing! Yep. Gotta prepare before you can go out into the wilderness...
                switch (selection) {
                    // $script:1227192907012254$
                    // - It's okay to be scared.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1227192907012255$ 
                // - I'm not scared! I'm c-cautious, okay? This is an important j-j-j-job. I'm <i>definitely</i> not stalling!
                return true;
            default:
                return true;
        }
    }
}
