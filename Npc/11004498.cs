using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004498: Lyton
/// </summary>
public class _11004498 : NpcScript {
    internal _11004498(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012384$ 
                // - Who's there? Oh, you're that... that $MyPCName$ hero! 
                return true;
            case 10:
                // $script:1227192907012385$ 
                // - Who's there? Oh, you're that... that $MyPCName$ hero! 
                switch (selection) {
                    // $script:1227192907012386$
                    // - What are you doing here?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012387$ 
                // - I'm the foremost cultural anthropologist of Sky Fortress, here to study the cultures of Kritias. And I feel I've already made a great discovery! 
                // $script:1227192907012388$ 
                // - I've uncovered some ancient writings here, and the motifs and archetypes on display are similar to those in ancient Victoria Island literature. Uncannily so. 
                switch (selection) {
                    // $script:1227192907012389$
                    // - That seems a little unlikely.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1227192907012390$ 
                // - It begs the question: do our cultures share the same root? Of course, the higher-ups will only accept evidence that our culture came first, and that Kritias copied us... 
                return true;
            default:
                return true;
        }
    }
}
