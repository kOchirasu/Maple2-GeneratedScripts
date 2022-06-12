using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001294: Dunba
/// </summary>
public class _11001294 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1215203907005008$
    // - Sigh... I should have left well enough alone...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1227194507005634$
                // - Ugh... He's the champ for a reason...
                return 40;
            case (40, 1):
                // $script:1227194507005635$
                // - If he'd gone all-out...
                switch (selection) {
                    // $script:1227194507005636$
                    // - What happened to you?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1227194507005637$
                // - Vasara Chen happened... He's the champion of the underground fighting circuit, and the son of Wei Hong. You know, the mob boss of Blackstar? He promised... promised that if I beat him, Blackstar would leave me alone...
                switch (selection) {
                    // $script:0131151207007895$
                    // - Soooooooo... the results?
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:0131151207007896$
                // - It ended with my utter defeat, as you can see. He said he had fun and that the Blackstars wouldn't bother me if I stayed down. Well, all it took was a single punch and I was done. I don't deserve to be the champion of Ludari Arena.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
