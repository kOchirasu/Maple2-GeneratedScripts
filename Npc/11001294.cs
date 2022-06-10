using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001294: Dunba
/// </summary>
public class _11001294 : NpcScript {
    internal _11001294(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215203907005008$ 
                // - Sigh... I should have left well enough alone...
                return true;
            case 40:
                // $script:1227194507005634$ 
                // - Ugh... He's the champ for a reason...
                // $script:1227194507005635$ 
                // - If he'd gone all-out...
                switch (selection) {
                    // $script:1227194507005636$
                    // - What happened to you?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1227194507005637$ 
                // - Vasara Chen happened... He's the champion of the underground fighting circuit, and the son of Wei Hong. You know, the mob boss of Blackstar? He promised... promised that if I beat him, Blackstar would leave me alone...
                switch (selection) {
                    // $script:0131151207007895$
                    // - Soooooooo... the results?
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:0131151207007896$ 
                // - It ended with my utter defeat, as you can see. He said he had fun and that the Blackstars wouldn't bother me if I stayed down. Well, all it took was a single punch and I was done. I don't deserve to be the champion of Ludari Arena.
                return true;
            default:
                return true;
        }
    }
}
