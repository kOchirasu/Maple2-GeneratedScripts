using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001027: Palace Warden
/// </summary>
public class _11001027 : NpcScript {
    internal _11001027(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003503$ 
                // - What seems to be the problem?
                return true;
            case 30:
                // $script:0831180407003506$ 
                // - Criminals are held here while waiting for sentencing. Once sentenced, they're sent to $map:02000124$.
                return true;
            default:
                return true;
        }
    }
}
