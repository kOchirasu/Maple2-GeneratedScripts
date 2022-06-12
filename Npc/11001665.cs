using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001665: Karl
/// </summary>
public class _11001665 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;30
    }

    // Select 0:
    // $script:0617211107006378$
    // - So, it's you.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0617211107006379$
                // - The empress has placed her faith in you.
                return -1;
            case (20, 0):
                // $script:0617211107006380$
                // - Your eyes speak volumes about your character, $MyPCName$. I believe I can trust you. We are depending on you to protect the peace of Maple World.
                return -1;
            case (30, 0):
                // $script:0426090007008441$
                // - What does Her Highness see in this stranger...?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
