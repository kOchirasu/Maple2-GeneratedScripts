using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001732: Entrance Door
/// </summary>
public class _11001732 : NpcScript {
    internal _11001732(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0728022507006977$ 
                // - Accessing system. Confirming credentials...
                return true;
            case 30:
                // $script:0728024607006978$ 
                // - Security systems will be put online if you do not verify your credentials. Failure to connect will require you to re-verify your credentials at the front gate.
                return true;
            default:
                return true;
        }
    }
}
