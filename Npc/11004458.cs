using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004458: Cantata
/// </summary>
public class _11004458 : NpcScript {
    internal _11004458(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1231140707012480$ 
                // - Hey there! I'm investigating rumors of a ghost dressed in black.
                return true;
            case 10:
                // $script:1231140707012481$ 
                // - Hey there! I'm investigating rumors of a ghost dressed in black.
                switch (selection) {
                    // $script:1231140707012482$
                    // - Did you say gh-gh-gh-ghost?!
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1231140707012483$ 
                // - Yes! There have been lots of sightings of this so-called black-garbed ghost around here.
                // $script:1231140707012484$ 
                // - Apparently it wanders around, mumbling something about sacrificing a soul to obtain great power...
                // $script:1231140707012485$ 
                // - It's right around this time that most of the witnesses run for their lives, so that's all I have to go on. Well, that, and...
                switch (selection) {
                    // $script:1231140707012486$
                    // - There's something else?
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1231140707012487$ 
                // - Yes! I think there was something about... summoning a many-armed god?
                switch (selection) {
                    // $script:1231140707012488$
                    // - It can't be...
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:1231140707012489$ 
                // - You know what that means?
                switch (selection) {
                    // $script:1231140707012490$
                    // - I'm sure it's nothing.
                    case 0:
                        Id = 14;
                        return false;
                }
                return true;
            case 14:
                // $script:1231140707012491$ 
                // - I'll let you know if I learn anything else. This investigation is just getting started!
                return true;
            case 20:
                // $script:0410153807014589$ 
                // - Hm...
                // $script:0410153807014590$ 
                // - Where oh where could it be?
                // $script:0410153807014591$ 
                // - Was I misled?
                return true;
            default:
                return true;
        }
    }
}
