using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004499: Mauritius
/// </summary>
public class _11004499 : NpcScript {
    internal _11004499(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012393$ 
                // - Hmm...? Have we met?
                return true;
            case 10:
                // $script:1227192907012394$ 
                // - Hmm...? Have we met?
                switch (selection) {
                    // $script:1227192907012395$
                    // - I came here on Sky Fortress.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012396$ 
                // - Oh, you're that famous hero! An honor to meet you.
                // $script:1227192907012397$ 
                // - I'm part of the architectural research team. Take a look at this structure here! Incredible, isn't it? I've never seen such an elaborate design.
                // $script:1227192907012398$ 
                // - Each brick and pillar fits perfectly. I've never seen something like this before.
                // $script:1227192907012399$ 
                // - All of the buildings I've examined since we got here has been like this. I only wish I could see how they pulled this off!
                switch (selection) {
                    // $script:0114163707012719$
                    // - I'm a bit curious, too.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0114163707012720$ 
                // - It's worth researching. This could revolutionize building techniques all over the empire.
                return true;
            default:
                return true;
        }
    }
}
