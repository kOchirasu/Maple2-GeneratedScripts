using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004508: Mannstad Sentry
/// </summary>
public class _11004508 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1228182607012446$
    // - Zzz... N-no... I can't eat another bite...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1228182607012447$
                // - Zzz... N-no... I can't eat another bite...
                switch (selection) {
                    // $script:1228182607012448$
                    // - <b>Hello there!</b>
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1228182607012449$
                // - <b>Aaaah!</b> Don't hurt me! I-I mean... I'm awake. I'm awake!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
