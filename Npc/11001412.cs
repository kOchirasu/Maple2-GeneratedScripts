using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001412: Sumsum
/// </summary>
public class _11001412 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1217205907005409$
    // - So... much... pain...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1222203907005501$
                // - C-can't... talk... Too... busy... pain...
                switch (selection) {
                    // $script:1222203907005502$
                    // - Where does it hurt?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1222203907005503$
                // - Leave me alone... you dummy... I need to rest...
                switch (selection) {
                    // $script:1222203907005504$
                    // - Hey, I'm just trying to help!
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:1222203907005505$
                // - G-go away... I don't want... your help... 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
