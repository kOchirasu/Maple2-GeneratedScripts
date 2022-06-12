using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001731: Informant M
/// </summary>
public class _11001731 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0728022507006976$
    // - Did you find me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0804172907007069$
                // - You see me? You have exceptionally sharp senses.
                switch (selection) {
                    // $script:0804172907007070$
                    // - What are you doing here?
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:0804172907007071$
                // - Where's it written I've got to tell you anything?
                switch (selection) {
                    // $script:0804172907007072$
                    // - Just curious.
                    case 0:
                        return 41;
                    // $script:0804172907007073$
                    // - Come on, tell me!
                    case 1:
                        return 42;
                }
                return -1;
            case (41, 0):
                // $script:0804172907007074$
                // - You may have enough free time to bug strangers, but I don't. Scram.
                return -1;
            case (42, 0):
                // $script:0804172907007075$
                // - Let me think... No.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            (42, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
