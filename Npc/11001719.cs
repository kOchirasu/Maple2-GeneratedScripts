using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001719: Junta
/// </summary>
public class _11001719 : NpcScript {
    internal _11001719(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0728022507006970$ 
                // - You have something to say to me?
                return true;
            case 30:
                // $script:0728024507007016$ 
                // - If things are to return to normal, then we must stay united. Don't forget that.
                return true;
            default:
                return true;
        }
    }
}
