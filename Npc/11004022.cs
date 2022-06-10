using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004022: Mysterious Bladesman
/// </summary>
public class _11004022 : NpcScript {
    internal _11004022(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010031$ 
                // - Don't talk to me.
                return true;
            case 20:
                // $script:0614185307010032$ 
                // - Go away, you bother me.
                return true;
            default:
                return true;
        }
    }
}
