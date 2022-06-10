using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004497: Axelrodi
/// </summary>
public class _11004497 : NpcScript {
    internal _11004497(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012376$ 
                // - I'm part of the team researching the fish of Kritias. 
                return true;
            case 10:
                // $script:1227192907012377$ 
                // - I'm part of the team researching the fish of Kritias. 
                // $script:1227192907012378$ 
                // - The water here is highly toxic. Just a sip would tombstone an ordinary person. But see in there? Fish. 
                switch (selection) {
                    // $script:1227192907012379$
                    // - How is that possible?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012380$ 
                // - I can't say anything conclusively just yet, but I think the aetherine in their bodies somehow protects them from the poison. 
                // $script:1227192907012381$ 
                // - Did the fish here evolve to use the aetherine to neutralize the poison? 
                switch (selection) {
                    // $script:0114163707012717$
                    // - That's pretty handy.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0114163707012718$ 
                // - Well, it's just a theory. 
                return true;
            default:
                return true;
        }
    }
}
