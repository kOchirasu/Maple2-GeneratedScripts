using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001555: Valen
/// </summary>
public class _11001555 : NpcScript {
    internal _11001555(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0415104107006021$ 
                // - How may I help you?
                return true;
            case 40:
                // $script:0421104907006047$ 
                // - Tsk. If people keep taking pebbles home as souvenirs, soon the beach will be completely bare.
                // $script:0421104907006048$ 
                // - This one time, somebody climbed the hill in the middle of the night to get up close to the whale. Or he tried to, but he lost his grip halfway up and fell. It was a total disaster.
                return true;
            default:
                return true;
        }
    }
}
