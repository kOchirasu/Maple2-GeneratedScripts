using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001239: Daon
/// </summary>
public class _11001239 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1123154807004442$
    // - Bah! What do I do?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1123154807004445$
                // - The grownups said not to leave the forest. But why not? What's out there? I gotta know!
                switch (selection) {
                    // $script:1123154807004446$
                    // - You should listen to the grownups, kid.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1123154807004447$
                // - But they never let me do anything fun! I bet there's all kinds of toys and games beyond the forest, and the grownups are keeping it all to themselves!
                switch (selection) {
                    // $script:1123154807004448$
                    // - Yeah, that's not it.
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:1123154807004449$
                // - Then maybe there's... there's just groves and groves of sweet fruit! There's got to be <i>something</i> out there! And I wanna see it!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
