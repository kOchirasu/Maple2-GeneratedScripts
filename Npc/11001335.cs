using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001335: Tizzy
/// </summary>
public class _11001335 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217012607005259$
    // - Oh, wait...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217012607005262$
                // - I forgot to return the board I rented and road it all the way home. I don't want to go all the way back to the rental place... Maybe I should just buy one for myself.
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
