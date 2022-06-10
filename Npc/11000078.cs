using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000078: Muphaza
/// </summary>
public class _11000078 : NpcScript {
    internal _11000078(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000366$ 
                // - How may I help you? 
                return true;
            case 10:
                // $script:0831180407000367$ 
                // - The wolves of the Vayar Mountains protect the tribes that worship the wolf god. We gray wolves are the guardians of the Murpagoths. The red wolves are the guardians of the Yamarchas. 
                return true;
            default:
                return true;
        }
    }
}
