using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001403: Racafony
/// </summary>
public class _11001403 : NpcScript {
    internal _11001403(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217025910001349$ 
                // - Let's see, what else can I do for fun around here?
                return true;
            case 30:
                // $script:1223143510001425$ 
                // - Is there something I can do for you?
                switch (selection) {
                    // $script:1223143510001426$
                    // - I want to go to <font color="#ffd200">Victoria Island</font>.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:1223143510001427$
                    // - ...
                    case 1:
                        Id = 34;
                        return false;
                }
                return true;
            case 31:
                // $script:1223143510001428$ 
                // - A-ha, you came to board the <i>Lumiwind</i>! Perfect timing... we're nearly done with maintenance. Did you want to depart right away?
                switch (selection) {
                    // $script:1223143510001429$
                    // - Yes.
                    case 0:
                        Id = 32;
                        return false;
                    // $script:1223143510001430$
                    // - I'll come back later.
                    case 1:
                        Id = 33;
                        return false;
                }
                return true;
            case 32:
                // $script:1223143510001431$ functionID=1 
                // - All right, bon voyage!
                return true;
            case 33:
                // $script:1223143510001432$ 
                // - Huh? So you don't want to fly? Okay. Well, let me know if you change your mind.
                return true;
            case 34:
                // $script:1223143510001433$ 
                // - Let me know if I can help.
                return true;
            default:
                return true;
        }
    }
}
