using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003267: Allon
/// </summary>
public class _11003267 : NpcScript {
    internal _11003267(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008214$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0403155707008217$ 
                // - I am captain of the Royal Guard. Each and every one of my men would lay down his life in service to Empress $npcName:11000075[gender:1]$.
                return true;
            default:
                return true;
        }
    }
}
