using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001363: Mika
/// </summary>
public class _11001363 : NpcScript {
    internal _11001363(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215222907005046$ 
                // - It's been too long since we gathered like this. 
                return true;
            case 10:
                // $script:1230171207005753$ 
                // - You can return the necklace... later, and in person! 
                return true;
            default:
                return true;
        }
    }
}
