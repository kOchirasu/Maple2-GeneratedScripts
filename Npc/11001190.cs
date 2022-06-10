using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001190: Blackstar Gangster
/// </summary>
public class _11001190 : NpcScript {
    internal _11001190(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1015162707004157$ 
                // - What brings you here?
                return true;
            case 30:
                // $script:1015162707004160$ 
                // - Trying to steal a Blackstar train? They've got to be crazy!
                return true;
            default:
                return true;
        }
    }
}
