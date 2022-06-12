using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004369: Claus
/// </summary>
public class _11004369 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109213607011781$
    // - I grow my own trees to decorate, you know. My commitment to the holidays cannot be questioned.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011782$
                // - My favorite memory from my childhood is decorating our tree every year. Now that I tend the garden myself, it can be even grander.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
