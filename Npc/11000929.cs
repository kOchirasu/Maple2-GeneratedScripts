using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000929: JJ Tutor
/// </summary>
public class _11000929 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003298$
    // - How did you find this place?!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003301$
                // - The saga of a thousand-year-old turtle writer. That's got to be a story worth telling!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
