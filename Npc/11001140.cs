using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001140: Gadren
/// </summary>
public class _11001140 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0911192907003908$
    // - What brings you to $map:02000110$?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0911192907003911$
                // - There's nothing more important than safety. Wouldn't you agree?
                switch (selection) {
                    // $script:0911192907003912$
                    // - I guess, sure.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0911192907003913$
                // - I know, right? But nobody else seems to get it! I see people come to work without their hard hats or work boots every day. Your goal should be to earn a living without killing yourself in the process!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
