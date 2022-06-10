using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001731: Informant M
/// </summary>
public class _11001731 : NpcScript {
    internal _11001731(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0728022507006976$ 
                // - Did you find me?
                return true;
            case 30:
                // $script:0804172907007069$ 
                // - You see me? You have exceptionally sharp senses.
                switch (selection) {
                    // $script:0804172907007070$
                    // - What are you doing here?
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:0804172907007071$ 
                // - Where's it written I've got to tell you anything?
                switch (selection) {
                    // $script:0804172907007072$
                    // - Just curious.
                    case 0:
                        Id = 41;
                        return false;
                    // $script:0804172907007073$
                    // - Come on, tell me!
                    case 1:
                        Id = 42;
                        return false;
                }
                return true;
            case 41:
                // $script:0804172907007074$ 
                // - You may have enough free time to bug strangers, but I don't. Scram.
                return true;
            case 42:
                // $script:0804172907007075$ 
                // - Let me think... No.
                return true;
            default:
                return true;
        }
    }
}
